FROM imzoe/texlive-full-inkscape-ubuntu

COPY batch_compile.py /batch_compile.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]