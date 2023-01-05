---
title: Convertir des données numériques de texte en nombre
type: docs
weight: 900
url: /fr/net/convert-text-numeric-data-to-number/
description: Apprenez à convertir des nombres stockés sous forme de texte dans Excel en nombres en utilisant le Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
{{% alert color="primary" %}}

 Parfois, vous souhaitez convertir des données numériques saisies sous forme de texte en nombres. Vous pouvez saisir des nombres sous forme de texte dans Excel Microsoft en mettant une apostrophe avant un nombre, par exemple**'12345**. Excel traite ensuite le nombre comme une chaîne. Aspose.Cells vous permet de convertir des chaînes en nombres.

{{% /alert %}}

Aspose.Cells fournit le[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)méthode qui peut être utilisée pour convertir toutes les données numériques de chaîne ou de texte en nombres.

 La capture d'écran suivante montre les numéros de chaîne dans les cellules**A1: A17**. Les numéros de chaîne sont alignés à gauche.

|**Fichier d'entrée : nombres saisis sous forme de chaînes de texte**|
|:- |
|![tâche : image_autre_texte](convert-text-numeric-data-to-number_1.png)|

Ces numéros de chaîne ont été convertis en nombres à l'aide de[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)dans la capture d'écran suivante. Comme vous pouvez le voir, ils sont maintenant alignés à droite.

|**Fichier de sortie : les chaînes ont été converties en nombres**|
|:- |
|![tâche : image_autre_texte](convert-text-numeric-data-to-number_2.png)|

## C# code pour convertir les données numériques de la chaîne en nombres réels

L'exemple de code suivant montre comment convertir toutes les données numériques de chaîne en nombres réels dans toutes les feuilles de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
