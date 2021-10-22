//
//  FFTerm
//  View media in the terminal.
//  Copyright Patrick Huang 2021
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <https://www.gnu.org/licenses/>.
//

#include <string>
#include <vector>


namespace Argparse {


/**
 * KwArg argument
 * e.g. --arg, --arg=1, --arg="asdf"
 */
struct KwArg {
    KwArg(std::vector<std::string> kwds);

    /**
     * Get human-readable string containing keywords.
     * e.g. "kwd1", "{kwd1|kwd2}", "{}"
     */
    std::string kwdstr();

    /**
     * Possible values to set the arg.
     */
    std::vector<std::string> kwds;

    /**
     * String value the user set.
     * Inited after parser.parse();
     */
    std::string value;
};

struct Parser {
    Parser(std::string description);

    /**
     * Add a keyword argument.
     */
    void add_kwarg(KwArg arg);

    /**
     * Print help to stderr.
     */
    void print_help(char** argv);

    std::string description;

    std::vector<KwArg> kwargs;
};


}  // namespace Argparse
