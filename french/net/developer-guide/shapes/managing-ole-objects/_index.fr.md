---
title: Gestion des objets OLE
type: docs
weight: 50
url: /fr/net/managing-ole-objects/
---
## **Introduction**

OLE (Object Linking and Embedding) est le cadre de Microsoft pour une technologie de document composé. En bref, un document composé est quelque chose comme un bureau d'affichage qui peut contenir des objets visuels et informatifs de toutes sortes : texte, calendriers, animations, son, vidéo animée, 3D, actualités continuellement mises à jour, commandes, etc. Chaque objet de bureau est une entité de programme indépendante qui peut interagir avec un utilisateur et également communiquer avec d'autres objets sur le bureau.

 OLE (Object Linking and Embedding) est pris en charge par de nombreux programmes différents et est utilisé pour rendre le contenu créé dans un programme disponible dans un autre. Par exemple, vous pouvez insérer un document Word Microsoft dans Excel Microsoft. Pour voir les types de contenu que vous pouvez insérer, cliquez sur**Objet** sur le**Insérer** menu. Seuls les programmes installés sur l'ordinateur et prenant en charge les objets OLE apparaissent dans la**Type d'objet** boîte.

### **Insertion d'objets OLE dans la feuille de calcul**

Aspose.Cells prend en charge l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells a le[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) classe, utilisée pour ajouter un nouvel objet OLE à la liste de collection. Une autre classe,[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), représente un objet OLE. Il compte quelques membres importants :

-  Le[**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)La propriété spécifie les données d'image (icône) de type tableau d'octets. L'image s'affichera pour montrer l'objet OLE dans la feuille de calcul.
-  Le[**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)La propriété spécifie les données de l'objet sous la forme d'un tableau d'octets. Ces données seront affichées dans son programme associé lorsque vous double-cliquez sur l'icône de l'objet OLE.

L'exemple suivant montre comment ajouter un ou plusieurs objets OLE dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Extraction d'objets OLE dans le classeur**

L'exemple suivant montre comment extraire des objets OLE dans un classeur. L'exemple obtient différents objets OLE à partir d'un fichier XLS existant et enregistre différents fichiers (DOC, XLS, PPT, PDF, etc.) en fonction du type de format de fichier de l'objet OLE.

Après avoir exécuté le code, nous pouvons enregistrer différents fichiers en fonction de leurs types de format d'objets OLE respectifs.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Extraction du fichier MOL intégré**

Aspose.Cells prend en charge l'extraction d'objets de types peu courants tels que MOL (fichier de données moléculaires contenant des informations sur les atomes et les liaisons). L'extrait de code suivant montre comment extraire le fichier MOL intégré et l'enregistrer sur le disque à l'aide de ceci[exemple de fichier excel](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Sujets avancés**
- [Accéder et modifier l'étiquette d'affichage de l'objet Ole lié](/cells/fr/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Actualiser automatiquement l'objet OLE via Microsoft Excel en utilisant Aspose.Cells](/cells/fr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraire les objets OLE du classeur](/cells/fr/net/extract-ole-objects-from-workbook/)
- [Obtenir ou définir l'identificateur de classe de l'objet OLE intégré](/cells/fr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Insertion d'un fichier WAV en tant qu'Objet Ole](/cells/fr/net/inserting-a-wav-file-as-an-ole-object/)

