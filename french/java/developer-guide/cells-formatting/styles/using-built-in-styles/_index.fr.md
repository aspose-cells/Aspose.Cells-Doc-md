---
title: Utilisation des styles intégrés
type: docs
weight: 480
url: /fr/java/using-built-in-styles/
---
{{% alert color="primary" %}} 

Aspose.Cells fournit une vaste collection de styles réutilisables pour formater une cellule dans un document de feuille de calcul. Nous pouvons utiliser des styles intégrés dans notre classeur et également créer des styles personnalisés.

{{% /alert %}} 
## **Comment utiliser les styles intégrés**
 La méthode[Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\) ) et classe[BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType)rendre pratique la création de styles réutilisables. Voici une liste de tous les styles intégrés possibles :

- [VINGT_POUR CENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [VINGT_POUR CENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [VINGT_POUR CENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [VINGT_POUR CENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [VINGT_POUR CENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [VINGT_POUR CENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [QUARANTE_POUR CENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [QUARANTE_POUR CENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [QUARANTE_POUR CENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [QUARANTE_POUR CENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [QUARANTE_POUR CENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [QUARANTE_POUR CENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [SOIXANTE_POUR CENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [SOIXANTE_POUR CENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [SOIXANTE_POUR CENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [SOIXANTE_POUR CENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [SOIXANTE_POUR CENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [SOIXANTE_POUR CENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [MAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [CALCUL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [CHECK_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [VIRGULE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [VIRGULE_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [DEVISE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [CURRENCY_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [EXPLICATION_TEXTE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [BIEN](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [HEADER_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [HEADER_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [HEADER_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [HEADER_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [HYPERLIEN](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [FOLLOWED_HYPERLINK](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [CONTRIBUTION](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [LINKED_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [NEUTRE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [ORDINAIRE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [REMARQUE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [PRODUCTION](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [POUR CENT](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [TITRE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [TOTAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [AVERTISSEMENT_TEXTE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [ROW_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [COLUMN_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

Le code suivant montre comment utiliser les styles intégrés.

![tâche : image_autre_texte](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
