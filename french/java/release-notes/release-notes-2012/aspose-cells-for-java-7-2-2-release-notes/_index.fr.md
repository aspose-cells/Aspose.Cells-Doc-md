---
title: Aspose.Cells for Java 7.2.2 Notes de mise à jour
type: docs
weight: 60
url: /fr/java/aspose-cells-for-java-7-2-2-release-notes/
---
{{% alert color="primary" %}} 

 Cette page contient des notes de version pour[Aspose.Cells for Java 7.2.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.2.2/)

{{% /alert %}} 

Nous sommes
 heureux d'annoncer Aspose.Cells for Java v7.2.2 !

 Nouvelles fonctionnalités

- Recherche de texte RegEx pour la méthode Cells.Find()

 Améliorations

- Rendre Aspose.Cells compatible avec les anciennes versions des bocaux Woodstox
- Les fichiers OOXML intégrés OLE dans XLS sortent en tant que fichiers empaquetés OLE au lieu de fichiers décompressés
- Prend en charge ExportObjectListener pour enregistrer les fichiers HTML
- Copier la mise en forme conditionnelle lors de la copie de lignes

 Des exceptions

- Picture.isPrintable() pour Picture inPageSetup provoque NullPointerException
- L'enregistrement d'un classeur chiffré avec un tableau croisé dynamique provoque une exception java.lang.NegativeArraySizeException

 Insectes

- Cells.importCustomObjects() avec le format DateTime spécifié ne fonctionne pas
- Mauvais type de graphique du graphique en nuage de points
- La double valeur perd en précision lors de la lecture du fichier de modèle CSV
- La série de graphiques est inversée lors de sa conversion en image
- Le fichier XLSX réenregistré provoque l'erreur "Excelfound unreadable content…"
- Le tableau croisé dynamique enregistré a causé "ProtectionView" lors de son ouverture dans MS Excel
- Utilisation de la validation de liste par Aspose.Cellscreates un fichier XLS qui ne fonctionne pas après la modification du séparateur de listes du système
