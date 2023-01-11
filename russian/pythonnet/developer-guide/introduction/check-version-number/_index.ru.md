﻿---
title: Проверить номер версии
type: docs
weight: 80
url: /ru/python-net/check-version-number/
---
{{% alert color="primary" %}}

Интересно, какую версию Aspose.Cells вы используете? Мы регулярно публикуем новые версии Aspose.Cells как для добавления новых функций, так и для устранения проблем. Номер версии состоит из основного номера версии, дополнительного номера версии и номера версии исправления. Каждое число должно быть целым числом от 0 и выше. Формат следующий:

основное.второстепенное.исправление

Когда мы выпускаем новую сборку Aspose.Cells, мы обновляем номер версии.

В этой статье объясняется, как проверить, какая версия Aspose.Cells установлена в системе вручную и с помощью файла Aspose.Cells API.

{{% /alert %}}

## **Проверить номер версии вручную**

Чтобы узнать, какую версию Aspose.Cells вы используете вручную:

1.  Щелкните правой кнопкой мыши файл Aspose.Cells.dll и выберите**Характеристики**.
1. Щелкните вкладку Версия (или Сведения), чтобы проверить номер версии.

## **Проверьте номер версии, используя Aspose.Cells API**

Чтобы узнать, какую версию Aspose.Cells вы используете через API, используйте статический метод GetVersion класса CellsHelper, чтобы получить номер версии Aspose.Cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CheckVersionNumber.py" >}}