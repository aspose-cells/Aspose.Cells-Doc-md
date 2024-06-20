---
title: Paramètres pour GridJs
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/settings/
description: Cet article décrit le paramétrage de GridJs.
keywords: paramètres,excel,classeur,gridjs,éditeur
---


Il existe certains paramètres que nous pouvons spécifier en définissant GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


Par exemple, le code suivant définit ReCalculateOnOpen sur false pour arrêter le calcul à l'ouverture du fichier :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 le code suivant définit l'auteur du fichier :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
Vous pouvez vérifier plus de paramètres dans cette classe.

