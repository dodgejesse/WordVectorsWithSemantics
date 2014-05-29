#!/usr/bin/env Rscript


library(plyr)
library(ggplot2)
library(scales)
library(gridExtra)
require(gridExtra)


d <- read.table('/home/jessed/jessed/pgm_project/WordVectorsWithSemantics/results/to_plot/full_data_four_cols.csv', sep=',')
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("men","MEN-3k",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("rg","RG-65",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("ws","WS-353",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("toefl","TOEFL",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("syn","SYN-REL",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("sent","SA",x) else x))

d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("ppdb","PPDB",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("wn\\+","WordNet",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("fn","FrameNet",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("union","Union",x) else x))

d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("fd","Multi   ",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("hu", "GC   ",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("lsa","LSA   ",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("mik","SG   ",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("nce","LBL   ",x) else x))

d$task = factor(d$V2, levels = c('MEN-3k', 'RG-65', 'WS-353', 'TOEFL', 'SYN-REL', 'SA'))
d$onto <- factor(d$V1, levels = c('PPDB', 'WordNet', 'FrameNet', 'Union'))




pdf('plots_facet.pdf')
ggplot(d, aes(V3,V4)) + geom_bar(stat = "identity", aes(fill = V3)) + guides(fill = guide_legend(title = NULL, title.position = "top")) + facet_grid(onto~task) + theme_bw() + theme(axis.title.x = element_blank(), axis.title.y = element_blank(), axis.text.x = element_blank(), axis.ticks.x=theme_blank(), strip.background =  theme_rect(fill = NA, colour = NA), plot.margin = unit(c(0,0,0,0),"cm")) + opts(legend.position = "bottom")
dev.off()

