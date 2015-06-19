#!/usr/bin/env python

"""
WhatIsCode

This extremely simple script was an inspiration driven by a combination of
Paul Ford's article on Bloomberg Business Week, "What is Code?"[1] and
Haddaway's song, "What is Love"[2].

[1] http://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/
[2] https://en.wikipedia.org/wiki/What_Is_Love_%28Haddaway_song%29


Usage Instructions/Examples:

    In a REPL or other program:

        # Import the module.
        from what_is_code import WhatIsCode

        # Instantiate the object.
        song = WhatIsCode()

        # Output the song.
        song.sing()


    As a standalone script on the shell:

        Make sure the script is executable:
        chmod +x what_is_code.py

        Run the script:
        ./what_is_code.py

Enjoy! :-)


Copyright 2015 Carlo Costino

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

class WhatIsCode(object):
    def __init__(self):
        """
        Initialize the main refrain and verses used throughout the song.
        """

        self.main_refrain = [
            'What is code?',
            'Program don\'t crash now',
            'Don\'t crash now, again',
        ]

        self.first_verse = [
            'I don\'t know why you don\'t work',
            'I type things in right, but you just fail',
            'So what is True?',
            'And what is False?',
            'Gimme a break',
        ]

        self.second_verse = [
            'Oh, I give up, nothing I do',
            'Will work in this app, that I called foo',
            'I wrote some tests',
            'And they all pass',
            'But my app fails',
        ]

        self.third_verse = [
            'Can you please just work, just work as I want',
            'This is insane, wasted time',
            'I thought this was easy, I though this was simple',
            'Is it code?',
        ]


    @property
    def secondary_refrain(self):
        """
        The secondary refrain is just the last two parts of the main refrain.
        """

        return self.main_refrain[1:]


    @property
    def tertiary_refrain(self):
        """
        A tertiary refrain appears once toward the end of the song made up of
        a substring of the last line in the main refrain.
        """

        return [self.main_refrain[2][:-7]] * 2


    @property
    def what_is_code(self):
        """
        "What is code?" is repeated many times throughout the song, so let's
        make it easy to repeat on its own.
        """

        return self.main_refrain[0]


    def sing_line(self, line=''):
        """
        Outputs a single string with a newline character at the end for proper
        formatting.
        """

        return '%s\n' % line


    def sing_lines(self, lines=[]):
        """
        Outputs a list of strings with a newline character at the end of each
        string, including the last one.
        """

        return '%s\n' % '\n'.join(lines)


    def sing(self):
        """
        Sings the entire song by printing out every line found within it.

        Yes, this is brute force and somewhat ugly, but also simple.
        """

        print(self.sing_lines(self.main_refrain))
        print(self.sing_lines(self.secondary_refrain))
        print(self.sing_line(self.what_is_code))
        print('Damn it\n')
        print(self.sing_lines(self.first_verse))
        print(self.sing_lines(self.main_refrain))
        print(self.sing_lines(self.main_refrain))
        print(self.sing_lines(self.second_verse))
        print(self.sing_lines(self.main_refrain))
        print(self.sing_lines(self.main_refrain))
        print(self.sing_line(self.what_is_code))
        print(self.sing_line(self.what_is_code))
        print(self.sing_lines(self.main_refrain))
        print(self.sing_lines(self.tertiary_refrain))
        print(self.sing_lines(self.third_verse))
        print(self.sing_lines(self.main_refrain))
        print(self.sing_lines(self.main_refrain))
        print('Damn\n')
        print(self.sing_lines(self.main_refrain))
        print(self.sing_lines(self.main_refrain))
        print(self.sing_lines(self.secondary_refrain))
        print(self.sing_lines(self.secondary_refrain))
        print(self.sing_line(self.what_is_code))


# If this module is being run as a standalone script, output the song
# immediately.
if __name__ == '__main__':
    song = WhatIsCode()
    song.sing()
