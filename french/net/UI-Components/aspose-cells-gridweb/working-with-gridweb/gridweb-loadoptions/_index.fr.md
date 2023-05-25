---
title: Options de chargement pour GridWeb
type: docs
weight: 90
url: /fr/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

Il existe certaines options de chargement que nous pouvons définir avant d'importer le fichier.

 on peut utiliser[GridLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)(pour dossier général) et[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) (pour le fichier csv)
 
{{% /alert %}} 
##  ** charger avec un autre encodage**
Pour le fichier csv, il s'agit en fait d'un fichier texte, sans l'encodage spécifique décrit dans le fichier au format xlsx.

Par conséquent, les utilisateurs peuvent définir un codage de caractères spécifique avant de charger le fichier.

voici un exemple de code à charger avec le chinois :

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```