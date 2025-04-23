---
title: Extraire les objets OLE du classeur
type: docs
weight: 110
url: /fr/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Parfois, vous devez extraire les objets OLE d'un classeur. Aspose.Cells prend en charge l'extraction et l'enregistrement de ces objets Ole.

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

### **Téléchargez et installez Aspose.Cells**

1. [Téléchargez Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installez-le sur votre ordinateur de développement.

Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.

### **Créer un projet**

Démarrez **Visual Studio.Net** et créez une nouvelle application console. Cet exemple montrera une application console C#, mais vous pouvez également utiliser VB.NET.

1. Ajouter des références
   1. Ajoutez une référence au composant Aspose.Cells à votre projet, par exemple ajoutez une référence à ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Extraire des objets OLE**

Le code ci-dessous fait le travail effectif de trouver et d'extraire des objets OLE. Les objets OLE (fichiers DOC, XLS et PDF) sont enregistrés sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
