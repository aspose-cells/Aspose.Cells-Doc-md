---
title: Importer des données à partir du document
type: docs
weight: 20
url: /fr/net/import-data-from-document/
---

Les données sont la collection de faits bruts et nous créons des documents de feuille de calcul ou des rapports pour présenter ces faits bruts de manière plus significative. Normalement, nous ajoutons des données aux feuilles de calcul par nous-mêmes, mais parfois, nous devons réutiliser des ressources de données existantes et c'est là que se situe le besoin d'importer des données dans les feuilles de calcul à partir de différentes sources de données. Dans ce sujet, nous discuterons de quelques techniques pour importer des données dans des feuilles de calcul à partir de différentes sources de données.

**Importation de données à l'aide de Aspose.Cells** 
Lorsque vous utilisez **Aspose.Cells** pour ouvrir un fichier Excel, toutes les données du fichier sont automatiquement importées, mais Aspose.Cells prend également en charge l'importation de données à partir de différentes sources de données. Quelques-unes de ces sources de données sont énumérées ci-dessous :

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells fournit une classe, **Workbook** qui représente un fichier Excel. La classe Workbook contient une collection de feuilles de calcul (Worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit une collection de cellules (Cells).

La collection de cellules (Cells) fournit des méthodes très utiles pour importer des données à partir de différentes sources de données.

Cette section comporte les sujets suivants:

- [Importation à partir d'un tableau](/cells/fr/net/importing-from-array/)
- [Importation à partir d'une ArrayList](/cells/fr/net/importing-from-arraylist/)
- [Importation à partir d'objets personnalisés](/cells/fr/net/importing-from-custom-objects/)
- [Importation à partir d'un DataTable](/cells/fr/net/importing-from-datatable/)
{{< app/cells/assistant language="csharp" >}}
