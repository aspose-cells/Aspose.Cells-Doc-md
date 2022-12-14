---
title: Aspose.Cells for Java 7.3.3 Notes de mise à jour
type: docs
weight: 20
url: /fr/java/aspose-cells-for-java-7-3-3-release-notes/
---
{{% alert color="primary" %}} 

 Cette page contient des notes de version pour[Aspose.Cells for Java 7.3.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.3/)

{{% /alert %}} 

Nous sommes
 heureux d'annoncer Aspose.Cells for Java v7.3.3 !

 Nouvelles fonctionnalités

- Ajoutez la méthode Row.getLastDataCell() pour obtenir la dernière cellule contenant des données dans une ligne
- Nouvelles API ajoutées pour obtenir le même Styleobject pour les cellules avec les mêmes paramètres de style

 Améliorations

- Ajoutez des guillemets aux valeurs de cellules vides lors de l'exportation d'un CSV avec

 option

 Exceptions

- La mise en forme conditionnelle avec des caractères Unicode échoue
- La définition de la formule avant d'ajouter des zones pour la mise en forme conditionnelle, puis de renommer la feuille de calcul a provoqué une erreur lors de l'enregistrement du classeur
- La ré-enregistrement d'un fichier de modèle XLS a provoqué une exceptionNegativeArraySizeException

 Insectes

- La valeur de la date formatée était différente de celle affichée dans MS Excel
- Les noms des séries de graphiques sont perdus siCellCollection est effacé
- L'affichage vide sous forme d'espaces/zéros ne fonctionne pas pour les fichiers XLSX
- Le formatage des étiquettes de données pour les graphiques n'est pas correct
- Le soulignement de la police a disparu dans le fichier PDF rendu
- La définition des styles de police n'a eu aucun effet pour XLSX en mode LightCells
- Une partie du pied de page a été perdue lors de l'enregistrement au format PDF
