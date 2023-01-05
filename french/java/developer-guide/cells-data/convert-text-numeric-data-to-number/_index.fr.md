---
title: Convertir des données numériques de texte en nombre
type: docs
weight: 150
url: /fr/java/convert-text-numeric-data-to-number/
description: Apprenez à convertir des nombres stockés sous forme de texte en nombres en utilisant le Aspose.Cells for Java API.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
{{% alert color="primary" %}}

 Parfois, vous souhaitez convertir des données numériques saisies sous forme de texte en nombres. Vous pouvez saisir des nombres sous forme de texte dans Excel Microsoft en mettant une apostrophe avant un nombre, par exemple**'12345**. Excel traite ensuite le nombre comme une chaîne. Aspose.Cells vous permet de convertir des chaînes en nombres.

{{% /alert %}}

Aspose.Cells for Java API fournit le[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) méthode qui peut être utilisée pour convertir toutes les données numériques de chaîne ou de texte en nombres.

 La capture d'écran suivante montre les numéros de chaîne dans les cellules**A1: A17**. Les numéros de chaîne sont alignés à gauche.

**Fichier d'entrée : nombres saisis sous forme de chaînes de texte** 

![tâche : image_autre_texte](convert-text-numeric-data-to-number_1.png)

Ces numéros de chaîne ont été convertis en nombres à l'aide de[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) dans la capture d'écran suivante. Comme vous pouvez le voir, ils sont maintenant alignés à droite.

**Fichier de sortie : les chaînes ont été converties en nombres** 

![tâche : image_autre_texte](convert-text-numeric-data-to-number_2.png)

L'exemple de code suivant montre comment convertir toutes les données numériques de chaîne en nombres réels dans toutes les feuilles de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
