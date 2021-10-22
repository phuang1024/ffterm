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

#include <iostream>

#include "argparse.hpp"


namespace Argparse {


KwArg::KwArg(std::vector<std::string> kwds) {
    this->kwds = kwds;
}

std::string KwArg::kwdstr() {
    if (kwds.size() == 0) {
        return "{}";
    } else if (kwds.size() == 1) {
        return kwds[0];
    } else {
        std::string str = "{";
        for (int i = 0; i < kwds.size(); i++) {
            str += kwds[i];
            if (i != kwds.size()-1)
                str += "|";
        }
        str += "}";
        return str;
    }
}


Parser::Parser(std::string description) {
    this->description = description;
}

void Parser::add_kwarg(KwArg arg) {
    kwargs.push_back(arg);
}

void Parser::print_help(char** argv) {
    std::cerr << "Usage: " << argv[0] << " ";
    for (KwArg& arg: kwargs) {
        std::cerr << arg.kwdstr() << " ";
    }
    std::cerr << std::endl;
}


}  // namespace Argparse
