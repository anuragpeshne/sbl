(* lexer *)

datatype token = EOF of pos * pos
               | NUM of pos * pos
               | LPAREN of pos * pos
               | RPAREN of pos * pos
               | PLUS of pos * pos;

fun scan (tokens, []) = (tokens, []:char list)
  | scan (tokens, (#"("::cs)) = scan (LPAREN::tokens, cs)
  | scan (tokens, (#")"::cs)) = scan (RPAREN::tokens, cs)
  | scan (tokens, (c::cs)) = if isIden c then
                                 scan (
                                     let idenStr (v, rest) = scanIden (#"", (c::cs))
                                     in
                                         (((iden identStr)::tokens), rest)
                                     end
                                 )
                             else raise scanError;
