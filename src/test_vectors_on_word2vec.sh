# assumes locations are as follows:
original_loc="../vectors/original/"
enriched_loc="../vectors/ppdb_modified/"
scratch_dir="../scratch/"
results_dir="../results/"
word2vec="/home/jesse/Dropbox/CMU/graphical_models/project/word2vec/word2vec-read-only/"

#for vec_set in "FD-640" "Huang-50" "mik-sg-80" "NCE-80"
#do
#	python count_rows_and_cols.py ${original_loc}${vec_set}.txt ${scratch_dir}${vec_set}.rows_and_cols.txt
#	cat ${scratch_dir}${vec_set}.rows_and_cols.txt > ${scratch_dir}${vec_set}.txt.add_first_line
#	cat ${original_loc}${vec_set}.txt >> ${scratch_dir}${vec_set}.txt.add_first_line
#	../lib/convert-binary ${scratch_dir}${vec_set}.txt.add_first_line ${scratch_dir}${vec_set}.bin
#	${word2vec}compute-accuracy ${scratch_dir}${vec_set}.bin < ${word2vec}questions-words.txt > ${scratch_dir}${vec_set}.word2vec_eval.txt
#done

for vec_set in "mik-sg-80" #"FD-640" "Huang-50" "NCE-80" "NCE-OneStep-50m"
do
	python count_rows_and_cols.py ${enriched_loc}${vec_set}-enriched.txt ${scratch_dir}${vec_set}-enriched.rows_and_cols.txt
	cat ${scratch_dir}${vec_set}-enriched.rows_and_cols.txt > ${scratch_dir}${vec_set}-enriched.txt.add_first_line
	cat ${enriched_loc}${vec_set}-enriched.txt >> ${scratch_dir}${vec_set}-enriched.txt.add_first_line
	../lib/convert-binary ${scratch_dir}${vec_set}-enriched.txt.add_first_line ${scratch_dir}${vec_set}-enriched.bin
	${word2vec}compute-accuracy ${scratch_dir}${vec_set}-enriched.bin < ${word2vec}questions-words.txt > ${results_dir}${vec_set}-enriched.word2vec_eval.txt
done
