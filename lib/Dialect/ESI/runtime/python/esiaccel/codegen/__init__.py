#  Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
#  See https://llvm.org/LICENSE.txt for license information.
#  SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""Code generation from ESI manifests to source code.

This package only re-exports the public API. The implementation lives in the
sibling modules:

  * `generator` -- the `Generator` base, `CppGenerator`, the C++ type planner /
    emitter (`CppTypePlanner` / `CppTypeEmitter`), and the `run` CLI entry point.
  * `indented_writer` -- the `_IndentedWriter` used by the emitters.
  * `ports` -- the per-port-kind strategy table and its rendering helpers.
"""

from .generator import (Generator, CppGenerator, CppTypePlanner, CppTypeEmitter,
                        run)
# Re-exported for the port-kind golden tests (see tests/unit/test_codegen.py).
from .ports import (_PORT_KINDS, _BUNDLE_KIND, _render_scalar_find,
                    _render_indexed_find)

__all__ = [
    "Generator",
    "CppGenerator",
    "CppTypePlanner",
    "CppTypeEmitter",
    "run",
]
