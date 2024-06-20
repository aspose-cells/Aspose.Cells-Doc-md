---
title: Gestion des objets OLE
type: docs
weight: 50
url: /fr/net/managing-ole-objects/
---

## **Introduction**

OLE (Object Linking and Embedding) est le cadre de Microsoft pour une technologie de document composé. En bref, un document composé est quelque chose comme un bureau d'affichage qui peut contenir des objets visuels et d'information de toutes sortes : texte, calendriers, animations, son, vidéo en mouvement, 3D, actualités continuellement mises à jour, contrôles, etc. Chaque objet de bureau est une entité de programme indépendante qui peut interagir avec un utilisateur et communiquer avec d'autres objets sur le bureau.

OLE (Object Linking and Embedding) est pris en charge par de nombreux programmes différents et est utilisé pour rendre le contenu créé dans un programme disponible dans un autre. Par exemple, vous pouvez insérer un document Microsoft Word dans Microsoft Excel. Pour voir quels types de contenus vous pouvez insérer, cliquez sur **Objet** dans le menu **Insérer**. Seuls les programmes installés sur l'ordinateur et prenant en charge les objets OLE apparaissent dans la zone **Type d'objet**.

### **Insertion d'objets OLE dans la feuille de calcul**

Aspose.Cells prend en charge l'ajout, l'extraction et la manipulation des objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells possède la classe [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection), utilisée pour ajouter un nouvel objet OLE à la liste de collections. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), représente un objet OLE. Elle contient des membres importants.

- La propriété [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.
- La propriété [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) spécifie les données d'objet sous forme d'un tableau d'octets. Ces données seront affichées dans leur programme associé lorsque vous double-cliquez sur l'icône d'objet OLE.

L'exemple suivant montre comment ajouter un ou des objets OLE dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

### **Extraction d'objets OLE dans le classeur**

L'exemple suivant montre comment extraire des objets OLE dans un classeur. L'exemple récupère différents objets OLE à partir d'un fichier XLS existant et enregistre différents fichiers (DOC, XLS, PPT, PDF, etc.) en fonction du type de format de fichier de l'objet OLE.

Après l'exécution du code, nous pouvons enregistrer différents fichiers en fonction de leurs types de format respectifs des objets OLE.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-ExtractingOLEObjects-1.cs" >}}

### **Extraction des fichiers MOL intégrés**

Aspose.Cells prend en charge l'extraction d'objets de types non courants tels que MOL (fichier de données moléculaires contenant des informations sur les atomes et les liaisons). L'extrait de code suivant démontre l'extraction d'un fichier MOL incorporé et son enregistrement sur disque en utilisant ce [fichier excel d'exemple](94896196.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ExtractEmbeddedMolFile-1.cs" >}}

## **Sujets avancés**
- [Accéder et modifier l'étiquette d'affichage de l'objet Ole lié](/cells/fr/net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Rafraîchir automatiquement un objet OLE via Microsoft Excel en utilisant Aspose.Cells](/cells/fr/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraire des objets OLE du classeur](/cells/fr/net/extract-ole-objects-from-workbook/)
- [Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé](/cells/fr/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Insérer un fichier WAV en tant qu'objet Ole](/cells/fr/net/inserting-a-wav-file-as-an-ole-object/)

