---
title: Extraire les objets OLE du classeur
type: docs
weight: 110
url: /fr/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Parfois, vous devez extraire des objets OLE d’un classeur. Aspose.Cells pour Python via .NET supporte l’extraction et l’enregistrement de ces objets Ole.

Cet article montre comment créer une application console dans Visual Studio.Net et extraire différents objets OLE d'un classeur avec quelques lignes de code simples.

{{% /alert %}}

## **Extraire les objets OLE d'un classeur**

### **Création d'un classeur modèle**

1. Créé un classeur sous Microsoft Excel.
1. Ajoutez un document Microsoft Word, un classeur Excel et un document PDF en tant qu'objets OLE sur la première feuille de calcul.

|**Document de modèle avec des objets OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Ensuite, extrayez les objets OLE et enregistrez-les sur le disque dur avec leurs types de fichiers respectifs.

### **Extraire les objets OLE à l'aide de la bibliothèque Aspose.Cells pour Python Excel**

Le code ci-dessous fait le travail effectif de trouver et d'extraire des objets OLE. Les objets OLE (fichiers DOC, XLS et PDF) sont enregistrés sur le disque.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
