---
title: كيفية تثبيت libgdiplus في نظام التشغيل macOS
type: docs
description: يشرح هذا المقال كيفية تثبيت libgdiplus في نظام التشغيل macOS، مثل Monterey 12.4.
weight: 150
url: /ar/net/how-to-install-libgdiplus-in-macos/
---

## نظرة عامة

في بعض الحالات، قد تختار استخدام Aspose.Cells والاعتماد على مكتبة الرسومات System.Drawing.Common. يحدث هذا غالبًا في إصدارات أقدم من .netcore (على سبيل المثال .netcore31 أو أقدم).

نظرًا لحاجة مكتبة الرسومات System.Drawing.Common إلى الاعتماد على libgdiplus، يوجه هذا المقال حول كيفية تثبيت libgdiplus على macOS.

## تثبيت Homebrew في نظام التشغيل macOS

أولاً، يمكنك تثبيت Homebrew على macOS عبر تشغيل الأمر التالي في Terminal.

```cs

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

## تثبيت libgdiplus في نظام التشغيل macOS

بعد تثبيت Homebrew ، يمكنك تثبيت libgdiplus في macOS:

```cs

brew install mono-libgdiplus

```

## الحل الموصى به

بالنسبة لمنصات .NET6 (أو أحدث) ، يُقارن مع منصات سابقة (.netcore31 أو قبل ذلك) ، الفارق الهام هو حول مكتبة الرسومات. 
في هذا المستند الرسمي [Microsoft Document](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) ، يشرح للإصدارات .NET6 أو أحدث مكتبة الرسومات "System.Drawing.Common" ستدعم فقط على نظام التشغيل Windows ، ويقدم توصيات لاستبدال مكتبة الرسومات.

لذا، يوفر Aspose.Cells حلاً يعتمد على مكتبة الرسومات SkiaSharp على الأنظمة غير Windows. نوصي باستخدام مكتبة SkiaSharp كمكتبة على macOS، مما يعني أيضًا أنه لا حاجة لتثبيت libgdiplus.

لمعرفة كيفية تثبيت Aspose.Cells على الأنظمة غير Windows واستخدام SkiaSharp كمكتبة رسومات، يرجى الرجوع إلى المقال التالي:
[كيفية تشغيل Aspose.Cells لـ .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
