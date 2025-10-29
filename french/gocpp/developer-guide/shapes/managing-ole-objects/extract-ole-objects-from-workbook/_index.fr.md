---
title: Extraire les objets OLE du classeur avec Golang via C++
linktitle: Extraire les objets OLE du classeur
type: docs
weight: 110
url: /fr/go-cpp/extract-ole-objects-from-workbook/
description: Apprenez comment extraire les objets OLE d’un classeur en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Parfois, vous devez extraire des objets OLE d'un classeur. Aspose.Cells supporte l'extraction et la sauvegarde de ces objets OLE.

Cet article montre comment créer une application console dans Visual Studio et extraire différents objets OLE d'un classeur avec quelques lignes de code simples.

{{% /alert %}}

## **Extraire les objets OLE d'un classeur**

### **Création d'un classeur modèle**

1. Créez un classeur dans Microsoft Excel.
1. Ajoutez un document Microsoft Word, un classeur Excel et un document PDF en tant qu'objets OLE sur la première feuille.

|**Document de modèle avec des objets OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Ensuite, extrayez les objets OLE et sauvegardez-les sur le disque dur avec leurs types de fichiers respectifs.

### **Téléchargez et installez Aspose.Cells**

1. [Télécharger Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/).
1. Installez-le sur votre ordinateur de développement.

Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.

### **Créer un projet**

Démarrez **Visual Studio** et créez une nouvelle application console. Cet exemple montrera une application console C++.

1. Ajouter des références
   1. Ajoutez une référence au composant Aspose.Cells dans votre projet, par exemple, ajoutez une référence à ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Extraire des objets OLE**

Le code ci-dessous effectue le travail réel de recherche et d'extraction des objets OLE. Les objets OLE (fichiers DOC, XLS, et PDF) sont enregistrés sur le disque.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
