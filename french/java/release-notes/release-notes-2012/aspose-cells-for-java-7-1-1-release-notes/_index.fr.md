---
title: Aspose.Cells for Java 7.1.1 Notes de mise à jour
type: docs
weight: 90
url: /fr/java/aspose-cells-for-java-7-1-1-release-notes/
---
{{% alert color="primary" %}} 

 Cette page contient des notes de version pour[Aspose.Cells for Java 7.1.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.1.1/)

{{% /alert %}} 

Nous sommes
 heureux d'annoncer Aspose.Cells for Java v7.1.1 !

 Nouvelles fonctionnalités

- Vérifier si une colonne est vide

 Améliorations

- Enregistrement sur XLSX avec LightCells API en effectuant un rendu direct sur OutputStream

 Exceptions

- La méthode Cell.setHtmlString() lève NullPointerException
- La lecture d'un fichier de modèle XLSX lance une exception NullPointerException

 Insectes

- L'axe de catégorie secondaire du graphique SCATTER devient l'axe de texte
- Le contenu de la zone de texte n'a pas été rendu correctement
- La fonction ROUND ne peut pas arrondir une valeur supérieure à 922337,20
- Le graphique n'a pas été lu correctement à partir du fichier ODStemplate
- Format de numéro personnalisé : "jj.MM.aaaa" n'a pas été enregistré correctement pour le fichier ODS
- LineShape devient plus court dans le document PDF généré
