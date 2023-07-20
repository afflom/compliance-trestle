# Copyright (c) 2022 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Handle writing of inherited statements to markdown."""
import logging
from typing import Optional

from trestle.core.markdown.md_writer import MDWriter
from abc import ABC, abstractmethod
from trestle.common import const


logger = logging.getLogger(__name__)

class LeveragedStatements(ABC):

    def __init__(self):
        self._md_file: Optional[MDWriter] = None

    @abstractmethod
    def write_statement_md() -> None:
        """Writes inheritance information to a single markdown file"""

        # - If the statement markdown file exists
        #   - Copy the yaml header as the yaml header
        #   - Copy Satisfied statement
        # - Begin Writing
        # - Add the yaml header
        # - Add Provided description
        # - Add Responsibility description
        # - Add satifsied statement heading
        # - If Satisfied statement was copied
        #   - Add satisfied statement body
        # - Write the file



class StatementTree(LeveragedStatements):

    def __init__(self, provided_uuid: str, provided_description: str, responsibility_uuid: str, responsibility_description: str):
        """Initialize the class."""
        self.provided_uuid = provided_uuid
        self.provided_description = provided_description
        self.responsibility_uuid = responsibility_uuid
        self.responsibility_description = responsibility_description

    def write_statement_md(self, leveraged_statement_file: str) -> None:
        
        header_comment_dict = {const.TRESTLE_STATEMENT_TAG: const.YAML_LEVERAGED_COMMENT}

        self._md_file = MDWriter(leveraged_statement_file, header_comment_dict)
        
        self._md_file.write_out()




class StatementProvided(LeveragedStatements):

    def __init__(self, provided_uuid: str, provided_description: str):
        """Initialize the class."""
        self.provided_uuid = provided_uuid
        self.provided_description = provided_description

    def write_statement_md() -> None:
        """Method Placeholder"""



class StatementResponsibility(LeveragedStatements):

    def __init__(self, responsibility_uuid: str, responsibility_description: str):
        """Initialize the class."""
        self.responsibility_uuid = responsibility_uuid
        self.responsibility_description = responsibility_description

    def write_statement_md() -> None:
        """Method Placeholder"""
