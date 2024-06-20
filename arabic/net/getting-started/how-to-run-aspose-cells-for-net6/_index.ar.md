---
title: كيفية تشغيل Aspose.Cells for .Net6
type: docs
description: "كيفية تشغيل Aspose.Cells for .Net6."
weight: 138
url: /ar/net/how-to-run-aspose-cells-for-net6/
---

## نظرة عامة

بالنسبة لمنصات .NET6 (أو أحدث) ، يُقارن مع منصات سابقة (.netcore31 أو قبل ذلك) ، الفارق الهام هو حول مكتبة الرسومات. 
في هذا المستند الرسمي [Microsoft Document](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) ، يشرح للإصدارات .NET6 أو أحدث مكتبة الرسومات "System.Drawing.Common" ستدعم فقط على نظام التشغيل Windows ، ويقدم توصيات لاستبدال مكتبة الرسومات.

بالنسبة لمنتج Apose.Cells، قمنا بإجراء التقييم وقمنا بإكمال ترحيل مكتبة الرسومات. نحن نستخدم SkiaSharp بدلاً من System.Drawing.Common في أنظمة غير ويندوز، كما اقترح في وثائق مايكروسوفت الرسمية. يرجى ملاحظة أن هذا التغيير الحرج سيكون ساري المفعول في Aspose.Cells 22.10.1 أو أحدث لـ .Net6.

بالنسبة لـ .netcore31 أو قبل ذلك ، من أجل التوافق والاستقرار ، نحن نستخدم حاليًا مكتبة الرسومات "System.Drawing.Common". تعتمد الاعتماديات لـ .netcore31 أو قبل ذلك على ما يلي:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

## تشغيل Aspose.Cells for .Net6 على نظام التشغيل Windows

أولاً يمكنك إنشاء تطبيق .net6 باستخدام VS2022 ، ثم يمكنك اختيار خيارات التثبيت التالية:

### التثبيت من خلال Nuget

1. البحث عن Aspose.Cells من NuGet: [Aspose.Cells for .NET حزمة NuGet](https://www.nuget.org/packages/Aspose.Cells/). 
يمكنك أيضًا تثبيت Aspose.Cells من مدير حزم Nuget في VS2022.

2. "SkiaSharp" أو "System.Drawing.Common" سيتم تثبيتها تلقائيًا كتبعية لـ Aspose.Cells 22.10.1 أو في وقت لاحق لمنصات .Net6 ، والتي تعتمد على تكوين "نظام الوجهة" في مشروعك.
- قم بتعيين "هدف نظام التشغيل" إلى "Windows" لمشروعك، وستستخدم "System.Drawing.Common" كتبعية في نظام الويندوز الخاص بك لمشروع .Net6. في هذا التكوين، سيكون نتيجة الرسم أقرب إلى .netcore31 أو الإصدارات السابقة.
**![تكوين نظام OS الهدف](TargetOS.png)**
- قم بتعيين "هدف نظام التشغيل" إلى "None" أو خيارات أخرى لمشروعك، وستستخدم "SkiaSharp" كتبعية في نظام الويندوز الخاص بك لمشروع .Net6. *يرجى ملاحظة أن الإصدار الذي يستخدم "SkiaSharp" كتبعية لا يدعم ميزة الطباعة إلى الطابعة.*

### تثبيت من خلال msi أو DLL

1. [قم بتنزيل Aspose.Cells.msi أو DLL](https://releases.aspose.com/cells/net/)

2. قم بفتح دليل التثبيت أو دليل DLL، ثم حدد الخطوة 3 أو 4 أدناه:

3. قم بتحديد مجلد "net6.0-windows"، وأضف Aspose.Cells.dll فيه لتطبيق .net6 الخاص بك. ثم قم بإضافة الحزم التالية يدوياً إلى مشروع .net6 الخاص بك:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

بهذه الطريقة، ستستخدم "System.Drawing.Common" كتبعية في نظام الويندوز الخاص بك لمشروع .Net6. في هذا التكوين، سيكون نتيجة الرسم أقرب إلى .netcore31 أو الإصدارات السابقة.

4. قم بتحديد مجلد "net6.0"، وأضف Aspose.Cells.dll فيه لتطبيق .net6 الخاص بك. ثم قم بإضافة الحزم التالية يدوياً إلى مشروع .net6 الخاص بك:
- SkiaSharp, 2.88.6.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

بهذه الطريقة، ستستخدم "SkiaSharp" كتبعية في نظام الويندوز الخاص بك لمشروع .Net6. *يرجى ملاحظة أن الإصدار الذي يستخدم "SkiaSharp" كتبعية لا يدعم ميزة الطباعة إلى الطابعة.*
## تشغيل Aspose.Cells for .Net6 على نظام Linux

يرجى الإشارة إلى طريقة التثبيت على نظام الويندوز، يمكنك فقط تحديد SkiaSharp كتبعية لمكتبة الرسومات على نظام Linux.

ستحتاج إلى القيام بالعمليات الإضافية التالية لضمان استخدام صحيح للSkiaSharp تحت نظام Linux:

1. قم بتشغيل الأمر التالي في نظام Linux الخاص بك:
```
apt-get update && apt-get install -y libfontconfig1
```
أو
```
apk update && apk add fontconfig 
```

2. أضف حزم NuGet "SkiaSharp.NativeAssets.Linux 2.88.6" إلى مشروع .net6 الخاص بك.

3. أو يمكنك اختيار إضافة حزم NuGet "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.6" إلى مشروع .net6 الخاص بك، بدلاً من الخطوتين أعلاه.

### ملف Dockerfile مثالي لأوبونت

1. أضف حزم NuGet "SkiaSharp.NativeAssets.Linux 2.88.6" إلى مشروع .net6 الخاص بك.

2. استخدم ملف Dockerfile التالي:
{{< highlight plain >}}
# Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

# add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["Ubuntu_Docker.csproj", "."]
RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]
{{< /highlight >}}

### ملف Dockerfile مثالي لألبين

1. أضف حزم NuGet "SkiaSharp.NativeAssets.Linux 2.88.6" إلى مشروع .net6 الخاص بك.

2. استخدم ملف Dockerfile التالي:
{{< highlight plain >}}
#Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

# add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.16 AS build
WORKDIR /src
COPY ["Alpine_Docker.csproj", "."]
RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]
{{< /highlight >}}
