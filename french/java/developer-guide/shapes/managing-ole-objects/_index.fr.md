---
title: Gestion des objets OLE
type: docs
weight: 30
url: /fr/java/managing-ole-objects/
---

## **Introduction**

OLE (Object Linking and Embedding) est le cadre de Microsoft pour une technologie de document composé. En bref, un document composé est quelque chose comme un bureau d'affichage qui peut contenir des objets visuels et d'information de toutes sortes : texte, calendriers, animations, son, vidéo en mouvement, 3D, actualités continuellement mises à jour, contrôles, etc. Chaque objet de bureau est une entité de programme indépendante qui peut interagir avec un utilisateur et communiquer avec d'autres objets sur le bureau.

OLE (Object Linking and Embedding) est pris en charge par de nombreux programmes différents et est utilisé pour rendre le contenu créé dans un programme disponible dans un autre. Par exemple, vous pouvez insérer un document Microsoft Word dans Microsoft Excel. Pour voir quels types de contenus vous pouvez insérer, cliquez sur **Objet** dans le menu **Insérer**. Seuls les programmes installés sur l'ordinateur et prenant en charge les objets OLE apparaissent dans la zone **Type d'objet**.

## **Insertion d'objets OLE dans une feuille de calcul**

Aspose.Cells prend en charge l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells a la classe [**OleObjectCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObjectCollection), utilisée pour ajouter un nouvel objet OLE à la liste de collection. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/java/com.aspose.cells/OleObject), représente un objet OLE. Elle possède certains membres importants :

- [**ImageData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ImageData) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.
- [**ObjectData**](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ObjectData) spécifie les données d'objet sous forme de tableau d'octets. Ces données seront affichées dans leur programme associé lorsque vous double-cliquez sur l'icône de l'objet OLE.

L'exemple suivant montre comment ajouter un objet OLE dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-InsertingOLEObjects-1.java" >}}

## **Extraction d'objets OLE dans le classeur**

L'exemple suivant montre comment extraire des objets OLE dans un classeur. L'exemple récupère différents objets OLE à partir d'un fichier XLS existant et enregistre différents fichiers (DOC, XLS, PPT, PDF, etc.) en fonction du type de format de fichier de l'objet OLE.

Voici la capture d'écran du fichier XLS modèle, il contient différents objets OLE intégrés dans la première feuille de calcul.

**Le fichier modèle contient quatre objets OLE** 

![todo:image_alt_text](managing-ole-objects_1.png)

Après avoir exécuté le code, nous pouvons enregistrer différents fichiers en fonction de leurs types de format d'objet OLE respectifs. Les captures d'écran suivantes montrent certains des fichiers créés.

**Le fichier XLS extrait** 

![todo:image_alt_text](managing-ole-objects_2.png)

**Le fichier PPT extrait** 

![todo:image_alt_text](managing-ole-objects_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-ole-ExtractingOLEObjects-1.java" >}}

## **Extraction des fichiers MOL intégrés**

Aspose.Cells prend en charge l'extraction d'objets de types inhabituels comme le MOL (fichier de données moléculaires contenant des informations sur les atomes et les liaisons). L'extrait de code suivant montre comment extraire un fichier MOL intégré et l'enregistrer sur disque en utilisant ce [fichier Excel d'exemple](EmbeddedMolSample.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ExtractEmbeddedMolFile-1.java" >}}

## **Sujets avancés**
- [Accéder et modifier l'étiquette d'affichage de l'objet Ole lié](/cells/fr/java/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Rafraîchir automatiquement un objet OLE via Microsoft Excel en utilisant Aspose.Cells](/cells/fr/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Extraire des objets OLE du classeur](/cells/fr/java/extract-ole-objects-from-workbook/)
- [Obtenir ou définir l'identifiant de classe de l'objet OLE incorporé](/cells/fr/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
{{< app/cells/assistant language="java" >}}
