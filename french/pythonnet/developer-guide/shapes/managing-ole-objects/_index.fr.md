---
title: Gestion des objets OLE
type: docs
weight: 50
url: /fr/python-net/managing-ole-objects/
---

## **Introduction**

OLE (Object Linking and Embedding) est le cadre de Microsoft pour une technologie de document composé. En bref, un document composé est quelque chose comme un bureau d'affichage qui peut contenir des objets visuels et d'information de toutes sortes : texte, calendriers, animations, son, vidéo en mouvement, 3D, actualités continuellement mises à jour, contrôles, etc. Chaque objet de bureau est une entité de programme indépendante qui peut interagir avec un utilisateur et communiquer avec d'autres objets sur le bureau.

OLE (Object Linking and Embedding) est pris en charge par de nombreux programmes différents et est utilisé pour rendre le contenu créé dans un programme disponible dans un autre. Par exemple, vous pouvez insérer un document Microsoft Word dans Microsoft Excel. Pour voir quels types de contenus vous pouvez insérer, cliquez sur **Objet** dans le menu **Insérer**. Seuls les programmes installés sur l'ordinateur et prenant en charge les objets OLE apparaissent dans la zone **Type d'objet**.

### **Insertion d'objets OLE dans la feuille de calcul**

Aspose.Cells pour Python via .NET supporte l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. C'est pourquoi, Aspose.Cells pour Python via .NET a la classe [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection), utilisée pour ajouter un nouvel objet OLE à la liste de collection. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), représente un objet OLE. Elle possède quelques membres importants :

- La propriété [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.
- La propriété [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) spécifie les données d'objet sous forme d'un tableau d'octets. Ces données seront affichées dans leur programme associé lorsque vous double-cliquez sur l'icône d'objet OLE.

L'exemple suivant montre comment ajouter un ou des objets OLE dans une feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-InsertingOLEObjects-1.py" >}}

### **Extraction d'objets OLE dans le classeur**

L'exemple suivant montre comment extraire des objets OLE dans un classeur. L'exemple récupère différents objets OLE à partir d'un fichier XLS existant et enregistre différents fichiers (DOC, XLS, PPT, PDF, etc.) en fonction du type de format de fichier de l'objet OLE.

Après l'exécution du code, nous pouvons enregistrer différents fichiers en fonction de leurs types de format respectifs des objets OLE.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-ExtractingOLEObjects-1.py" >}}

### **Extraction des fichiers MOL intégrés**

Aspose.Cells pour Python via .NET supporte l'extraction d'objets de types peu courants comme MOL (fichier de données moléculaires contenant des informations sur les atomes et les liaisons). Le code ci-dessous démontre l'extraction d'un fichier MOL intégré et sa sauvegarde sur le disque en utilisant ce [fichier Excel d'exemple](94896196.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractEmbeddedMolFile-1.py" >}}

## **Sujets avancés**
- [Accéder et modifier l'étiquette d'affichage de l'objet Ole lié](/cells/fr/python-net/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Rafraîchissement automatique de l'objet OLE](/cells/fr/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraire des objets OLE du classeur](/cells/fr/python-net/extract-ole-objects-from-workbook/)
- [Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé](/cells/fr/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Insérer un fichier WAV en tant qu'objet Ole](/cells/fr/python-net/inserting-a-wav-file-as-an-ole-object/)

