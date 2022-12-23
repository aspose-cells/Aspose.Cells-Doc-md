---
title: Aspose.Cells for Java 7.2.1 Notes de mise à jour
type: docs
weight: 70
url: /fr/java/aspose-cells-for-java-7-2-1-release-notes/
---
{{% alert color="primary" %}} 

 Cette page contient des notes de version pour[Aspose.Cells for Java 7.2.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.2.1/)

{{% /alert %}} 

Nous sommes
 heureux d'annoncer Aspose.Cells for Java v7.2.1 !

 Nouvelles fonctionnalités

- Formater le tableau croisé dynamique avec des styles personnalisés pour différentes catégories (Modifier le style rapide du tableau croisé dynamique)

 Améliorations

- Cells.findString()/find() prend en charge la recherche de RegExand dans une plage spécifique
- Prise en charge de Picture.setTitle()/getTitle()
- Enregistrer les graphiques MS Excel dans le fichier ODS
- Rendre le fichier Aspose.Cells créé XLS compatible avec POI

 Des exceptions

- La lecture du fichier XLSX produit : "java.lang.ClassCastException:org.dom4j.Namespace"

 Insectes

- Le fichier XLSX enregistré donne l'erreur : "Datamay has been lost"
- Le numéro formaté était incorrect dans le PDF généré (mille caractères de groupe ont été perdus)
- Le graphique à barres n'apparaissait pas dans le PDF généré pour la version JDK6
- Les références ne sont pas mises à jour lors de l'extension d'une plage
