---
title: Aspose.Cells para iOS a través de Xamarin Limitaciones y API Diferencias
type: docs
weight: 10
url: /es/net/aspose-cells-for-ios-via-xamarin-limitations-and-api-differences/
---
## Es posible que la última versión de Aspose.Cells para iOS a través de Xamarin no funcione con la versión anterior de Xamarin.iOS
Tenga en cuenta que Aspose.Cells para iOS a través de Xamarin siempre se crea con las últimas versiones estables de las plataformas Xamarin y Xamarin.iOS. Si tiene algún problema al usar Aspose.Cells para iOS a través de Xamarin en su aplicación Xamarin.Android, asegúrese de tener instaladas las últimas versiones de Xamarin y Xamarin.iOS. A veces, Aspose.Cells para iOS a través de Xamarin se crea con la última versión de Xamarin (Xamarin.iOS) que no funciona con versiones anteriores de Xamarin.
## Aspose.Cells para iOS a través de las limitaciones de Xamarin
- Insertar imágenes: no compatible.
- Creación de gráficos: no compatible.
- Configuración de fondo degradado: no compatible.
- Agregar comentarios a las celdas: no compatible.
- Implementación de validaciones de datos: no compatible.
- Creación de saltos de página personalizados: no se admite.
- Implementación de marcadores inteligentes: no compatible.
- Proteger/desproteger hojas de trabajo: no compatible.
- Especificación de opciones de protección avanzada introducidas en Excel XP y versiones posteriores: no compatible.
- Inserción de controles de formulario y otras formas/objetos de dibujo: no compatible.
- Creación de tablas dinámicas y gráficos dinámicos: no se admite.
- Preservar o eliminar un complemento, VBA, macros: no compatible.
- Implementación de opciones de transposición: no compatible.
- Creación de gráficos personalizados - No compatible.
- Agregar, conservar o extraer objetos OLE de las hojas de cálculo: no se admite.
- Implementación de Microsoft chispas de Excel 2010: no compatible.
- Cifrado de archivos: no compatible.
## Público API (espacio de nombres) diferencias
En Aspose.Cells para iOS a través de Xamarin, se usa Aspose.Cells.Drawing namespace en lugar de System.Drawing en .NET API. La lista de objetos afectados es la siguiente:

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


