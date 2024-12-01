// add two numbers

function add(a, b: integer): integer;
begin
    add := a + b;
end;

var:
    a, b: integer;

begin

    a := 1;
    b := 2;

    writeln(add(a, b));
end.