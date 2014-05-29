#!/usr/bin/env Rscript


library(plyr)
library(ggplot2)
library(scales)
library(gridExtra)
require(gridExtra)


d <- read.table('/home/jessed/jessed/pgm_project/WordVectorsWithSemantics/results/to_plot/multi_data_three_cols.csv', sep=',')
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("men","MEN-3k",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("rg","RG-65",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("ws","WS-353",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("toefl","TOEFL",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("syn","SYN-REL",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("sent","SA",x) else x))

#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("ppdb","PPDB",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("wn\\+","WordNet",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("fn","FrameNet",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("union","Union",x) else x))

#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("mik","SG   ",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("LBL","LBL   ",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("LSA","LSA   ",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("hu", "   ",x) else x))
#d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("lsa","LSA   ",x) else x))

d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("Spanish MC-30","ES MC-30",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("French WS-353","FR WS-353",x) else x))
d <- as.data.frame(lapply(d,function(x) if(is.character(x)|is.factor(x)) gsub("German RG-65","DE RG-65",x) else x))

d$task = factor(d$V1, levels = c('FR WS-353', 'DE RG-65', 'ES MC-30'))
#d$onto <- factor(d$V1, levels = c('PPDB', 'WordNet', 'FrameNet', 'Union'))





pdf('plots_multi.pdf')
ggplot(d, aes(V2,V3)) + geom_bar(stat = "identity", aes(fill = V2)) + coord_cartesian(ylim=c(5,20)) + guides(fill = guide_legend(title = NULL, keysize = 20)) + facet_grid(~ task) + theme_bw() + theme(axis.title.x = element_blank(), axis.title.y = element_blank(), axis.text.x = element_blank(), axis.ticks.x=theme_blank(), axis.text.y = element_text(size=rel(2)), strip.background =  theme_rect(fill = NA, colour = NA), strip.text = element_text(size=rel(1.7)), plot.margin = unit(c(0,0,0,0),"cm"), legend.key.size = unit(1.5, "cm"), legend.text = element_text(size=rel(2))) + scale_fill_manual(values = c("LBL   " = "#A3A500", "SG" = "#E76BF3", "LSA   " = "#00BF7D"))
dev.off()

