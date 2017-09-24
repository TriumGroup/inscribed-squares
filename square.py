class Square:
    PADDING = 20

    @staticmethod
    def prepare_points(width, height, padding=PADDING):
        return [
            (padding, padding),
            (width - padding, padding),
            (width - padding, height - padding),
            (padding, height - padding)
        ]
