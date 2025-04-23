---
title: Ce format de fichier n est pas pris en charge ou vous ne spécifiez pas un format correct
type: docs
weight: 10
url: /fr/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **Ce format de fichier n'est pas pris en charge ou vous ne spécifiez pas un format correct**
Si l'utilisateur a spécifié le format de fichier lors de la création du classeur à partir du fichier modèle, cette erreur survient généralement parce que le format de fichier spécifié n'est pas le format de fichier réel du fichier modèle. Si l'utilisateur n'a pas spécifié le format de fichier, c'est généralement parce que l'extension du nom de fichier ne représente pas le format de fichier réel de ce fichier et que le format de fichier ne peut pas être détecté automatiquement, tel que le fichier csv/tsv qui n'a pas de marqueurs spéciaux.
{{< app/cells/assistant language="java" >}}
