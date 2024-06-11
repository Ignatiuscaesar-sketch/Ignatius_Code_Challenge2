import pytest
from classes.many_to_many import Band, Concert, Venue

class TestVenue:
    def test_has_name(self):
        venue = Venue(name="Ace of Spades", city="SAC")
        assert venue.name == "Ace of Spades"

    def test_name_is_mutable_string(self):
        venue_1 = Venue(name="Ace of Spades", city="SAC")
        assert isinstance(venue_1.name, str)
        venue_1.name = "MoonDust"
        assert isinstance(venue_1.name, str)
        assert venue_1.name == "MoonDust"
        with pytest.raises(ValueError):
            venue_1.name = 7

    def test_name_has_length(self):
        venue_1 = Venue(name="Ace of Spades", city="SAC")
        assert len(venue_1.name) > 0
        with pytest.raises(ValueError):
            venue_1.name = ""

    def test_has_city(self):
        venue = Venue(name="Ace of Spades", city="SAC")
        assert venue.city == "SAC"

    def test_city_is_mutable_string(self):
        venue_1 = Venue(name="Ace of Spades", city="SAC")
        assert isinstance(venue_1.city, str)
        venue_1.city = "NYC"
        assert isinstance(venue_1.city, str)
        assert venue_1.city == "NYC"
        with pytest.raises(ValueError):
            venue_1.city = 7

    def test_city_has_length(self):
        venue_1 = Venue(name="Ace of Spades", city="SAC")
        assert len(venue_1.city) > 0
        with pytest.raises(ValueError):
            venue_1.city = ""

    def test_concerts(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre Max", city="NYC")
        concert_1 = Concert(date="Nov 22", band=band, venue=venue)
        concert_2 = Concert(date="Nov 27", band=band, venue=venue)
        venue.add_concert(concert_1)
        venue.add_concert(concert_2)
        assert len(venue.concerts) == 2
        assert concert_1 in venue.concerts
        assert concert_2 in venue.concerts

    def test_concerts_of_type_concert(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre Max", city="NYC")
        concert_1 = Concert(date="Nov 22", band=band, venue=venue)
        concert_2 = Concert(date="Nov 27", band=band, venue=venue)
        venue.add_concert(concert_1)
        venue.add_concert(concert_2)
        assert all(isinstance(concert, Concert) for concert in venue.concerts)

    def test_bands(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue_1 = Venue(name="Theatre", city="NYC")
        concert_1 = Concert(date="Nov 22", band=band_1, venue=venue_1)
        concert_2 = Concert(date="Nov 27", band=band_2, venue=venue_1)
        venue_1.add_concert(concert_1)
        venue_1.add_concert(concert_2)
        assert len(venue_1.bands) == 2
        assert band_1 in venue_1.bands
        assert band_2 in venue_1.bands

    def test_bands_of_type_band(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue_1 = Venue(name="Theatre", city="NYC")
        concert_1 = Concert(date="Nov 22", band=band_1, venue=venue_1)
        concert_2 = Concert(date="Nov 27", band=band_2, venue=venue_1)
        venue_1.add_concert(concert_1)
        venue_1.add_concert(concert_2)
        assert all(isinstance(band, Band) for band in venue_1.bands)

    def test_bands_are_unique(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Triple Genius", hometown="LA")
        venue_1 = Venue(name="Theatre", city="NYC")
        concert_1 = Concert(date="Nov 22", band=band_1, venue=venue_1)
        concert_2 = Concert(date="Nov 27", band=band_2, venue=venue_1)
        concert_3 = Concert(date="Nov 29", band=band_2, venue=venue_1)
        venue_1.add_concert(concert_1)
        venue_1.add_concert(concert_2)
        venue_1.add_concert(concert_3)
        assert len(set(venue_1.bands)) == len(venue_1.bands)
        assert len(venue_1.bands) == 2
        assert band_1 in venue_1.bands
        assert band_2 in venue_1.bands

    def test_concert_on(self):
        """returns the first concert on that date or None if no concerts exist"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="SAC")
        concert_1 = band.play_in_venue(venue=venue, date="Nov 22")
        concert_2 = band.play_in_venue(venue=venue2, date="Nov 27")

        assert venue.concert_on("Nov 22") == concert_1
        assert venue2.concert_on("Nov 27") == concert_2
        assert venue.concert_on("Nov 25") is None

    # Uncommented lines
    def test_name_must_be_non_empty_string(self):
        with pytest.raises(ValueError):
            Venue(name=7, city="NYC")
        with pytest.raises(ValueError):
            Venue(name="", city="NYC")

    def test_city_must_be_non_empty_string(self):
        with pytest.raises(ValueError):
            Venue(name="Theatre", city=7)
        with pytest.raises(ValueError):
            Venue(name="Theatre", city="")
