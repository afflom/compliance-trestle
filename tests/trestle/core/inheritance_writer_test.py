# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2021 IBM Corp. All rights reserved.
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
"""Tests for control input output methods."""

import pathlib

import trestle.common.const as const
import trestle.core.inheritance_writer as inheritancewriter
from trestle.core.markdown.markdown_processor import MarkdownProcessor

provided_uuid = '18ac4e2a-b5f2-46e4-94fa-cc84ab6fe114'
provided_statement_desc = 'provided statement description'
resp_uuid = '4b34c68f-75fa-4b38-baf0-e50158c13ac2'
resp_statement_desc = 'resp statement description'


def test_write_inheritance_tree(tmp_path: pathlib.Path) -> None:
    """Test writing statements with both provided and responsibility."""
    statement_tree_path = tmp_path.joinpath('statementTree.md')

    statement = inheritancewriter.StatementTree(provided_uuid, provided_statement_desc, resp_uuid, resp_statement_desc)

    statement.write_statement_md(statement_tree_path)

    assert statement_tree_path.exists()


def test_write_inheritance_provided(tmp_path: pathlib.Path) -> None:
    """Test writing statements with only provided."""
    statement_provided_path = tmp_path.joinpath('statementProvided.md')

    statement = inheritancewriter.StatementProvided(provided_uuid, provided_statement_desc)

    statement.write_statement_md(statement_provided_path)

    assert statement_provided_path.exists()

    md_proc = MarkdownProcessor()

    assert md_proc.fetch_value_from_header(statement_provided_path, const.TRESTLE_LEVERAGING_COMP_TAG)


def test_write_inheritance_responsibility(tmp_path: pathlib.Path) -> None:
    """Test writing statements with only responsibility."""
    statement_resp_path = tmp_path.joinpath('statementReq.md')

    statement = inheritancewriter.StatementResponsibility(resp_uuid, resp_statement_desc)

    statement.write_statement_md(statement_resp_path)

    assert statement_resp_path.exists()

    md_proc = MarkdownProcessor()

    assert md_proc.fetch_value_from_header(statement_resp_path, const.TRESTLE_LEVERAGING_COMP_TAG)
