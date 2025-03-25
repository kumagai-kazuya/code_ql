/**
 * Sample: Check for variables declared but never used
 */
import javascript

from VariableDecl decl
where not exists (decl.getAReference())
select decl, "Unused variable detected."
