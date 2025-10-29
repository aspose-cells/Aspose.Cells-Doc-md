---
title: Ce format de fichier n est pas pris en charge ou vous ne spécifiez pas un format correct
type: docs
weight: 10
url: /fr/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **Ce format de fichier n'est pas pris en charge ou vous ne spécifiez pas un format correct**
Si l'utilisateur a spécifié le format du fichier lors de la création du classeur à partir d'un fichier modèle, cette erreur survient généralement parce que le format du fichier spécifié n'est pas le véritable format du fichier modèle. Si l'utilisateur n'a pas spécifié le format du fichier, c'est généralement parce que l'extension du nom de fichier ne correspond pas au véritable format de ce fichier et que le format du fichier ne peut pas être détecté automatiquement, comme le fichier csv/tsv qui ne possède pas d'identifiants spécifiques. Bien sûr, les formats de fichiers non supportés par Cells signaleront également cette erreur.
{{< app/cells/assistant language="java" >}}
