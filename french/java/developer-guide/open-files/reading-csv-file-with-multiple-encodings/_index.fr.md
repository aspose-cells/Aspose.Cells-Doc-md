---
title: Lecture du fichier CSV avec plusieurs encodages
type: docs
weight: 140
url: /fr/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

Parfois, votre fichier CSV contient plusieurs encodages (Unicode, ANSI, UTF8, UTF7, etc.). Aspose.Cells vous permet de charger ces fichiers CSV et de les convertir dans d'autres formats, par exemple PDF ou XLSX.

{{% /alert %}} 

 Aspose.Cells fournit la méthode TxtLoadOptions.setMultiEncoded(), que vous devez définir sur**vrai** pour charger correctement votre fichier CSV avec plusieurs encodages.

 La capture d'écran suivante montre un exemple de fichier CSV qui contient deux lignes. La première ligne est dans**ANSI** encodage et la deuxième ligne est dans**Unicode** codage

**Fichier d'entrée** 

![tâche : image_autre_texte](reading-csv-file-with-multiple-encodings_1.png)

La capture d'écran suivante montre le fichier XLSX converti à partir du fichier CSV ci-dessus sans définir la méthode TxtLoadOptions.setMultiEncoded() sur true. Comme vous pouvez le voir, le texte Unicode n'a pas été converti correctement.

**Fichier de sortie 1 : aucune adaptation n'a été faite pour l'encodage multiple** 

![tâche : image_autre_texte](reading-csv-file-with-multiple-encodings_2.png)

La capture d'écran suivante montre le fichier XSLX converti à partir du fichier CSV ci-dessus après avoir défini la méthode TxtLoadOptions.setMultiEncoded() sur true. Comme vous pouvez le voir, le texte Unicode est maintenant correctement converti.

**Fichier de sortie 2 : IsMultiEncoded est défini sur true** 

![tâche : image_autre_texte](reading-csv-file-with-multiple-encodings_3.png)

Vous trouverez ci-dessous l'exemple de code qui convertit correctement le fichier CSV ci-dessus au format XLSX.

**Java**

{{< highlight "csharp" >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
