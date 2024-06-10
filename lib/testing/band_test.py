import pytest
from classes.many_to_many import Band, Concert, Venue

class TestBand:
    def test_has_name(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="spicegurls", hometown="London")
        assert band_1.name == "boygenius"
        assert band_2.name == "spicegurls"

    def test_name_is_mutable_string(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        assert isinstance(band_1.name, str)
        band_1.name = "spicegurls"
        assert band_1.name == "spicegurls"
        with pytest.raises(ValueError):
            band_1.name = 7

    def test_name_has_length(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        assert len(band_1.name) > 0
        with pytest.raises(ValueError):
            band_1.name = ""

    def test_has_hometown(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="spicegurls", hometown="London")
        assert band_1.hometown == "NYC"
        assert band_2.hometown == "London"

    def test_hometown_is_immutable_string(self):
        band_1 = Band(name="boygenius", hometown="NYC")
        with pytest.raises(AttributeError):
            band_1.hometown = "Boston"

    def test_concerts(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        band.play_in_venue(venue, "Nov 22")
        band.play_in_venue(venue, "Nov 27")
        assert len(band.concerts) == 2

    def test_venues(self):
        band = Band(name="boygenius", hometown="NYC")
        venue1 = Venue(name="Theatre", city="NYC")
        venue2 = Venue(name="Ace of Spades", city="SAC")
        band.play_in_venue(venue1, "Nov 22")
        band.play_in_venue(venue2, "Nov 27")
        assert len(band.venues) == 2
        assert venue1 in band.venues
        assert venue2 in band.venues

    def test_venues_are_unique(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        band.play_in_venue(venue, "Nov 22")
        band.play_in_venue(venue, "Nov 27")
        assert len(set(band.venues)) == 1

    def test_play_in_venue(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert_1 = band.play_in_venue(venue, "Nov 22")
        assert len(band.concerts) == 1
        assert band.concerts[0] == concert_1
        assert isinstance(concert_1, Concert)

    def test_all_introductions(self):
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        band.play_in_venue(venue, "Nov 22")
        assert (
            band.all_introductions()[0]
            == "Hello NYC!!!!! We are boygenius and we're from NYC"
        )
