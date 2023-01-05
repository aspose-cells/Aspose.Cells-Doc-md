---
title: Aspose.Cells для iOS через ограничения Xamarin и различия API
type: docs
weight: 10
url: /ru/net/aspose-cells-for-ios-via-xamarin-limitations-and-api-differences/
---
## Последняя версия Aspose.Cells для iOS через Xamarin может не работать со старой версией Xamarin.iOS
Обратите внимание, что Aspose.Cells для iOS через Xamarin всегда создается с использованием последних стабильных версий платформ Xamarin и Xamarin.iOS. Если у вас возникнут проблемы при использовании Aspose.Cells для iOS через Xamarin в приложении Xamarin.Android, убедитесь, что у вас установлены последние версии Xamarin и Xamarin.iOS. Иногда Aspose.Cells для iOS через Xamarin создается с использованием последней версии Xamarin (Xamarin.iOS), которая не работает со старыми версиями Xamarin.
## Aspose.Cells для iOS через ограничения Xamarin
- Вставка изображений - не поддерживается.
- Создание диаграмм — не поддерживается.
- Настройка градиентного фона — не поддерживается.
- Добавление комментариев к ячейкам — не поддерживается.
- Реализация проверки данных — не поддерживается.
- Создание пользовательских разрывов страниц — не поддерживается.
- Реализация смарт-маркеров — не поддерживается.
- Защита/снятие защиты рабочих листов — не поддерживается.
- Указание расширенных параметров защиты, представленных в Excel XP и более поздних версиях — не поддерживается.
- Вставка элементов управления формы и других фигур/объектов рисования — не поддерживается.
- Создание сводных таблиц и сводных диаграмм — не поддерживается.
- Сохранение или удаление надстройки, VBA, макросов — не поддерживается.
- Реализация параметров транспонирования — не поддерживается.
- Создание пользовательских диаграмм — не поддерживается.
- Добавление, сохранение или извлечение объектов OLE из электронных таблиц — не поддерживается.
- Реализация искровых линий Excel 2010 Microsoft — не поддерживается.
- Шифрование файлов — не поддерживается.
## Общедоступные API (пространство имен) различия
В Aspose.Cells для iOS через Xamarin пространство имен Aspose.Cells.Drawing используется вместо System.Drawing в .NET API. Список затронутых объектов выглядит следующим образом:

- Aspose.Cells.Drawing.Color
- Aspose.Cells.Drawing.ColorConverter
- Aspose.Cells.Drawing.ColorTranslator
- Aspose.Cells.Drawing.FontStyle
- Aspose.Cells.Drawing.GraphicsUnit
- Aspose.Cells.Drawing.ImageFormatConverter
- Aspose.Cells.Drawing.KnownColor
- Aspose.Cells.Drawing.KnownColors
- Aspose.Cells.Drawing.Locale
- Aspose.Cells.Drawing.SystemColors
- Aspose.Cells.Drawing.Imaging.PixelFormat
- Aspose.Cells.Drawing.Imaging.ImageFormat
- Aspose.Cells.Drawing.Imaging.ImageFlags
- Aspose.Cells.Drawing.Drawing2D.SmoothingMode
- Aspose.Cells.Drawing.Drawing2D.PathPointType
- Aspose.Cells.Drawing.Drawing2D.PathData
- Aspose.Cells.Drawing.Drawing2D


