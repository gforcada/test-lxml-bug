<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    exclude-result-prefixes="xsl fo html saxon"
    >

  <xsl:output
      method="html"
      indent="yes"
      omit-xml-declaration="yes"
      />

  <xsl:template match="html|h2|p|strong|b|i|em|sup|sub|br">
    <xsl:copy>
      <xsl:apply-templates />
    </xsl:copy>
  </xsl:template>

  <!-- Convert all disallowed elements to paragraphs -->
  <xsl:template match="node()">
    <p>
      <xsl:apply-templates />
    </p>
  </xsl:template>

  <!-- Copy text -->
  <xsl:template match="text()">
    <xsl:value-of select="." />
  </xsl:template>

</xsl:stylesheet>

