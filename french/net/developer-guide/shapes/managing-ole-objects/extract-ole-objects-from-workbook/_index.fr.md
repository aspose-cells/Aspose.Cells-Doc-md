---
title: Extraire les objets OLE du classeur
type: docs
weight: 110
url: /fr/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

Parfois, vous devez extraire des objets OLE d'un classeur. Aspose.Cells prend en charge l'extraction et l'enregistrement de ces objets Ole.

Cet article montre comment créer une application console dans Visual Studio.Net et extraire différents objets OLE d'un classeur avec quelques lignes de code simples.

{{% /alert %}}

## **Extraire des objets OLE d'un classeur**

### **Création d'un modèle de classeur**

1. Création d'un classeur dans Microsoft Excel.
1. Ajoutez un document Word Microsoft, un classeur Excel et un document PDF en tant qu'objets OLE sur la première feuille de calcul.

|**Modèle de document avec des objets OLE (OleFile.xls)**|
|:- |
|![tâche : image_autre_texte](extract-ole-objects-from-workbook_1.png)|

Extrayez ensuite les objets OLE et enregistrez-les sur le disque dur avec leurs types de fichiers respectifs.

### **Téléchargez et installez Aspose.Cells**

1. [Télécharger Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installez-le sur votre poste de développement.

Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.

### **Créer un projet**

Démarrer**Visual Studio.Net** et créer une nouvelle application console. Cet exemple montre une application console C#, mais vous pouvez également utiliser VB.NET.

1. Ajouter des références
 1. Ajoutez une référence au composant Aspose.Cells à votre projet, par exemple ajoutez une référence à ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Extraire des objets OLE**

Le code ci-dessous effectue le travail réel de recherche et d'extraction d'objets OLE. Les objets OLE (fichiers DOC, XLS et PDF) sont enregistrés sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
