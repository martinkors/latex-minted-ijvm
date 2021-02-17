# LaTeX minted IJVM support

## How to use

Add the `ijvm.py` file to your Latex project (in the same folder your latex file).

Then to use the **IJVM** highlighting in minted write:
```
\begin{minted}{ijvm.py:IJVMLexer -x}
  ...
\end{minted}
```