from spaal2.core import DummyLidarVLP16, DummyOutdoor, DummySpooferContinuousPulse, visualize, PreciseDuration

def main():
    # generate arb
    csv = "out/dora_csv.csv"

    lidar = DummyLidarVLP16()
    outdoor = DummyOutdoor(
        wall_distance_m=50,
        reflectivity=0.5,
    )
    spoofer = DummySpooferContinuousPulse(
        frequency=1e6,
        pulse_width=PreciseDuration(nanoseconds=10),
    )

    point_list = []
    while True:
        try:
            config, signal = lidar.scan()

            if config.altitude == 900 and abs(config.azimuth - 100) < 20:
                spoofer.trigger(config, signal)

            signal = outdoor.apply(signal)
            signal += spoofer.get_range_signal(config.start_timestamp, config.accept_duration)
            points = lidar.receive(config, signal)
            point_list.extend(points)
        except StopIteration:
            break

    print(f"There are {len(point_list)} points.")
    visualize(point_list)


if __name__ == "__main__":
    main()
