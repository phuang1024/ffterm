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
 * Keyword argument
 * e.g. --arg, --arg=1, --arg="asdf"
 */
struct Keyword {
    Keyword(std::vector<std::string> kwds);

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
    void add_keyword(Keyword arg);

    std::string description;

    std::vector<Keyword> kwargs;
};


}  // namespace Argparse
