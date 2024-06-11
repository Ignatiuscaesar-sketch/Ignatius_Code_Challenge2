import pytest
from classes.many_to_many import Band, Concert, Venue

class TestConcert:
    def test_has_date(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)
        assert concert.date == "Nov 5"

    def test_date_is_mutable_string(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)
        concert.date = "Nov 15"
        assert isinstance(concert.date, str)
        assert concert.date == "Nov 15"
        with pytest.raises(ValueError):
            concert.date = 15

    def test_date_has_length(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)
        assert len(concert.date) > 0
        with pytest.raises(ValueError):
            concert.date = ""

    def test_has_venue(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)
        assert concert.venue == venue

    def test_venue_of_type_venue(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)
        with pytest.raises(ValueError):
            concert.venue = "My house"

    def test_venue_is_mutable(self):
        band = Band(name="boygenius", hometown="NYC")
        venue_1 = Venue(name="Theatre", city="NYC")
        venue_2 = Venue(name="House Extended", city="LA")
        concert = Concert(date="Nov 5", band=band, venue=venue_1)
        concert.venue = venue_2
        assert concert.venue == venue_2

    def test_has_band(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)
        assert concert.band == band

    def test_band_of_type_band(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)
        with pytest.raises(ValueError):
            concert.band = "My friends"

    def test_band_is_mutable(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="girlgenius", hometown="Boston")
        venue_1 = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band_1, venue=venue_1)
        concert.band = band_2
        assert concert.band == band_2

    def test_hometown_show(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="Sac")
        concert1 = band.play_in_venue(venue=venue, date="Nov 3")
        concert2 = band.play_in_venue(venue=venue2, date="Nov 5")
        assert concert1.hometown_show() is True
        assert concert2.hometown_show() is False

    def test_introduction(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="Sac")
        concert1 = band.play_in_venue(venue=venue, date="Nov 3")
        concert2 = band.play_in_venue(venue=venue2, date="Nov 5")
        assert (
            concert1.introduction() ==
            "Hello NYC!!!!! We are boygenius and we're from NYC"
        )
        assert (
            concert2.introduction() ==
            "Hello Sac!!!!! We are boygenius and we're from NYC"
        )

    def test_get_all_concerts(self):
        Concert.all = []
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="Sac")
        concert_1 = band.play_in_venue(venue=venue, date="Nov 3")
        concert_2 = band.play_in_venue(venue=venue2, date="Nov 5")
        assert len(Concert.all) == 2
        assert concert_1 in Concert.all
        assert concert_2 in Concert.all

    def test_date_must_be_non_empty_string(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        with pytest.raises(ValueError):
            Concert(date=15, band=band, venue=venue)
        with pytest.raises(ValueError):
            Concert(date="", band=band, venue=venue)

    def test_venue_must_be_instance_of_venue(self):
        band = Band(name="boygenius", hometown="NYC")
        with pytest.raises(ValueError):
            Concert(date="Nov 5", band=band, venue="My house")

    def test_band_must_be_instance_of_band(self):
        venue = Venue(name="Theatre", city="NYC")
        with pytest.raises(ValueError):
            Concert(date="Nov 5", band="My friends", venue=venue)
