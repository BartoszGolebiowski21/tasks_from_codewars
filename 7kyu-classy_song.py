# https://www.codewars.com/kata/6089c7992df556001253ba7d


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = []

    def how_many(self, array):
        new_listeners_count = 0
        for person in array:
            if person.lower() not in self.listeners:
                self.listeners.append(person.lower())
                new_listeners_count += 1
        return new_listeners_count


mount_moose = Song('Mount Moose', 'The Snazzy Moose')
final_countdown = Song('Final Countdown', 'Europe')


print(mount_moose.title)
print(mount_moose.artist)

# print(mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']))
# print(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']))

print(mount_moose.how_many(['joe', 'bob', 'joe', 'caleb', 'joe']))
print(mount_moose.listeners)
print(final_countdown.how_many(['tom', 'richard']))
print(final_countdown.listeners)
