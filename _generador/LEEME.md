# Generador del manual

Las páginas de cada plugin salen de `datos_calidad.py` y `datos_gestion.py` (una ficha por plugin) con la plantilla
`pagina.py` y el diagrama de `diagrama.py`. Para regenerar todo: `python3 _generador/generar.py` desde la raíz.
Si cambia un plugin, se cambia su ficha y se regenera (no editar los index.html a mano).
