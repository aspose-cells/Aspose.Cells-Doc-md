---
title: DeviceInfo dans le fichier rsreportserver.config
type: docs
weight: 70
url: /fr/reportingservices/deviceinfo-in-rsreportserver-config-file/
---

La section DeviceInfo dans **rsreportserver.config** prend les paramètres suivants qui affectent le comportement d'Aspose.Cells :

- **FileExtension** : lorsque la valeur est **null**, l'extension du fichier de rapport exporté est la valeur par défaut. Lorsque la valeur n'est pas null, l'extension du rapport est définie sur la valeur.
- **SimplePageHeaders** : lorsque la valeur est **true**, l'élément d'en-tête du rapport est rendu comme un en-tête de page Microsoft Excel. La valeur par défaut est **false**.
- **SimplePageFooters** : lorsque **true**, l'élément de pied de page du rapport est rendu comme un pied de page Microsoft Excel. La valeur par défaut est **true**.
- **PutoutHeader**: lorsque **true** (par défaut), l'élément d'en-tête du rapport est exporté. Lorsque **false**, l'élément d'en-tête du rapport n'est pas exporté. Ne prend en charge que l'extension Excel 2007 XLSX (données uniquement).
- **PutoutFooter**: lorsque **true** (par défaut), l'élément de pied de page du rapport est exporté. Lorsque **false**, il ne l'est pas. Ne prend en charge que l'extension Excel 2007 XLSX (données uniquement).
- **FillTableGroupHeaderForSimpleOutPut**: **false** par défaut. La valeur ne prend en charge que l'extension Excel 2007 XLSX (données uniquement).
- **NoOutPutTotalForSimpleOutPut**: **false** par défaut. La valeur ne prend en charge que l'extension Excel 2007 XLSX (données uniquement).
- **NoOutPutGroupForSimpleOutPut**: **false** par défaut. La valeur ne prend en charge que l'extension Excel 2007 XLSX (données uniquement).
- **NoDoGroupPageForSimpleOutPut**: **true** par défaut. La valeur ne prend en charge que l'extension Excel 2007 XLSX (données uniquement).
- **NoDoPageForSimpleOutPut**: **true** par défaut. La valeur ne prend en charge que l'extension Excel 2007 XLSX (données uniquement).
- **FieldDelimiter**: définit les délimiteurs de champ. La valeur prend en charge les extensions CSV et TXT.
