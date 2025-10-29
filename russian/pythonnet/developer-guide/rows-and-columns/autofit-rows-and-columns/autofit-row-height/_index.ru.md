---
title: Автоматическое подгонение высоты строки при загрузке файла
type: docs
weight: 120
url: /ru/python-net/autofit-row-height/
description: Узнайте, как подогнать строки, высота которых не настроена, с помощью Aspose.Cells для Python API via .NET.
keywords: Библиотека Excel на Python, автоматическое изменение высоты строки в Python при загрузке файла, автоматическое подгонение высоты строки при открытии файла Excel. 
---

## **Возможные сценарии использования**
Высота строки автоматически соответствует шрифту содержимого, но если высота кэшированной строки не совпадает с высотой содержимого в файле, MS Excel автоматически подгонит высоту строки при загрузке файла, в то время как Aspose.Cells для Python via .NET не будет автоматически ее подгонять для улучшения производительности. Если вам нужно использовать программу Aspose.Cells для Python via .NET для автоматического сопоставления высот строк при загрузке файлов, вы можете достичь цели с помощью параметра [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/).

Пожалуйста, обратитесь к следующим данным изображения. Мы видим, что высота кэшированной строки в строке 11 равна 15, но Excel автоматически подгоняет высоту строки при загрузке файла.
<br>
<img src="1.png" width=70% />

## **Настройка высоты строки с использованием библиотеки Excel для Python Aspose.Cells**
Если вы загружаете файл непосредственно и сохраняете его в формате PDF, данные не будут полностью отображены в PDF, потому что высота кэшированной строки равна только 15.
<br>
<img src="2.png" width=70% />
<br>
Если установить параметр [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) в значение true при загрузке файла, то Aspose.Cells для Python via .NET автоматически подгонит высоту строки. Настроенная высота строки эффективно соответствует требованиям текстового отображения.
<br>
<img src="3.png" width=70% />

## **Пример кода на Python**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
{{< app/cells/assistant language="python-net" >}}
