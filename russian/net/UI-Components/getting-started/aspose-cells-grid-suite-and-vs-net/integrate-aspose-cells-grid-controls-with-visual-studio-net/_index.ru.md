---
title: Интеграция элементов управления Aspose.Cells Grid с Visual Studio .NET
type: docs
weight: 10
url: /ru/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
description: Эта статья описывает, как использовать элементы управления GridWeb и GridDesktop в среде vissual studio .NET.
keywords:  GridWeb,GridDesktop,visual studio,control,integrate
---

{{% alert color="primary" %}} 

Разработчики Visual Studio.NET могут легко перетаскивать элементы управления из **Toolbox** на форму Windows или Web. Пакет Aspose.Cells Grid можно загрузить с помощью установщика MSI или в виде набора DLL-файлов. В этой статье объясняется, что нужно сделать, чтобы убедиться, что элементы управления Aspose.Cells.Grid могут быть использованы в Visual Studio.NET, когда он установлен с использованием DLL-файлов вместо установщика.

{{% /alert %}} 
## **Интегрировать элементы управления Aspose.Cells Grid с Visual Studio.NET**
Для интеграции элементов управления Aspose.Cells Grid с Visual Studio.NET:

1. Откройте Toolbox.
1. Выберите вкладку Общее (или любую другую вкладку, на которую вы хотите добавить элементы управления).
1. Щелкните правой кнопкой мыши на вкладке Общее.
1. В Visual Studio.NET выберите **Выбрать элементы** в меню. Появится диалоговое окно Настроить Toolbox (Этот процесс более или менее одинаков для новых версий среды разработки VS.NET (например, VS.NET 2013/2015 или более поздние)).
1. Нажмите **Обзор** и найдите файлы Aspose.Cells.GridDesktop.dll и Aspose.Cells.GridWeb.dll.
1. Выберите DLL-файлы, а затем нажмите **Открыть**. Диалоговое окно Настроить Toolbox теперь будет содержать элементы управления из пакета Aspose.Cells Grid. Новые добавленные элементы будут выделены в диалоговом окне.
1. Нажмите **OK**, чтобы добавить элементы управления в Toolbox Visual Studio.NET.

Элементы управления Aspose.Cells Grid будут добавлены на вкладку **Общее** в Toolbox. Только элемент управления GridWeb не активен. Это потому что мы работаем с приложением Windows Forms. GridWeb доступен только при работе с веб-формами, тогда как GridDesktop может использоваться только с формами Windows.
