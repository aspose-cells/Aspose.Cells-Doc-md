---
title: Options de chargement pour GridWeb
type: docs
weight: 90
url: /fr/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: option de chargement, options de chargement, paramétrage, options de chargement, option
description: Cet article présente comment travailler avec les options de chargement dans GridWeb.
---

{{% alert color="primary" %}} 

Il y a quelques options de chargement que nous pouvons définir avant d'importer le fichier.

nous pouvons utiliser [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (pour les fichiers généraux) et [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (pour les fichiers CSV)	

{{% /alert %}} 
## **chargement avec d'autres codages**
Pour le fichier CSV, il s'agit en fait d'un fichier basé sur du texte, sans l'encodage spécifique décrit dans le fichier au format xlsx.

Par conséquent, les utilisateurs peuvent définir un encodage de caractères spécifique avant de charger le fichier.

voici un code d'exemple pour charger avec du chinois :

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
