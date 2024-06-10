class Band:
    def __init__(self, name, hometown):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(hometown, str) or not hometown:
            raise ValueError("Hometown must be a non-empty string.")
        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    @property
    def concerts(self):
        return self._concerts

    @property
    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise ValueError("Provided venue must be an instance of Venue.")
        new_concert = Concert(date, self, venue)
        self._concerts.append(new_concert)
        venue.add_concert(new_concert)
        return new_concert

    def all_introductions(self):
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self._concerts
        ]

class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(city, str) or not city:
            raise ValueError("City must be a non-empty string.")
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("City must be a non-empty string.")
        self._city = value

    @property
    def concerts(self):
        return self._concerts

    def add_concert(self, concert):
        if not isinstance(concert, Concert):
            raise ValueError("Must add a Concert instance.")
        if concert not in self._concerts:  # Ensuring no duplicate concerts are added
            self._concerts.append(concert)

    @property
    def bands(self):
        return list(set(concert.band for concert in self._concerts))

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None

class Concert:
    all = []  # Ensure we keep track of all concerts

    def __init__(self, date, band, venue):
        if not isinstance(date, str) or not date:
            raise ValueError("Date must be a non-empty string.")
        if not isinstance(band, Band):
            raise ValueError("Band must be an instance of Band.")
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be an instance of Venue.")

        self._date = date
        self._band = band
        self._venue = venue
        Concert.all.append(self)  # Add the concert to the class attribute all

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Date must be a non-empty string.")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise ValueError("Band must be an instance of Band.")
        self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise ValueError("Venue must be an instance of Venue.")
        self._venue = value

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

