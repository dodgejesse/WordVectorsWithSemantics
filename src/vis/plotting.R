#!/usr/bin/env Rscript
#library(plyr)
#library(ggplot2)
#library(scales)
#dtf <- data.frame(x = c("ETB", "PMA", "PER", "KON", "TRA", 
#                  "DDR", "BUM", "MAT", "HED", "EXP"),
#                  y = c(.02, .11, -.01, -.03, -.03, .02, .1, -.01, -.02, 0.06))
#ggplot(dtf, aes(x, y)) +
#  geom_bar(stat = "identity", aes(fill = x), legend = FALSE) + 
#  geom_text(aes(label = paste(y * 100, "%"),
#               vjust = ifelse(y >= 0, 0, 1))) +
#  scale_y_continuous("Anteil in Prozent", labels = percent_format()) +
#  opts(axis.title.x = theme_blank())



#########################################################
library(plyr)
library(ggplot2)
library(scales)
library(gridExtra)
require(gridExtra)


ontos = c('ppdb', 'wn+', 'fn', 'union')

plots = list(list(),list(),list(),list(),list(),list())
loc = '/home/jessed/jessed/pgm_project/WordVectorsWithSemantics/results/to_plot/'
for (j in 1:length(ontos)){
    d <- read.csv(paste(paste(loc, ontos[j], sep=''),'.tsv', sep=''),sep='\t')




      for (i in 1:nrow(d)){
      	  dtf = data.frame(x = colnames(d), y = t(d[i,]))
    	  names(dtf) <- c("x","y")

	  plots[[i]][[j]] <- ggplot(dtf, aes(x,y)) + 
      	  	     geom_bar(stat = "identity", aes(fill = x), legend = FALSE) +
#      		     geom_text(aes(label = paste(y, "%"),
#		      vjust = ifelse(y >= 0, 0, 1))) +
      		     scale_y_continuous(limits = c(-14, 19)) +
      		     theme(axis.title.x = element_blank(), axis.title.y = element_blank(),
		     	   axis.text.x = element_blank(), axis.text.y = element_blank(), axis.ticks=theme_blank(), 
			   plot.margin = unit(c(.05,.05,.05,.05),"cm"))
      }
}

pdf('plots_full.pdf')
grid.arrange(plots[[1]][[1]],plots[[2]][[1]],plots[[3]][[1]],plots[[4]][[1]],plots[[5]][[1]],plots[[6]][[1]],
	plots[[1]][[2]],plots[[2]][[2]],plots[[3]][[2]],plots[[4]][[2]],plots[[5]][[2]],plots[[6]][[2]],
	plots[[1]][[3]],plots[[2]][[3]],plots[[3]][[3]],plots[[4]][[3]],plots[[5]][[3]],plots[[6]][[3]],
	plots[[1]][[4]],plots[[2]][[4]],plots[[3]][[4]],plots[[4]][[4]],plots[[5]][[4]],plots[[6]][[4]],
	ncol=nrow(d),nrow=4)
dev.off()