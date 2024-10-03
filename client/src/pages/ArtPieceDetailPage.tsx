// src/pages/ArtPieceDetailPage.tsx
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { getArtPiece, getReviews } from "../services/api";
import { ArtPiece, Review } from "../types";
import ReviewCard from "../components/ReviewCard";
import ArtPieceCard from "../components/ArtPieceCard";
import { Button } from "@/components/ui/button";

const ArtPieceDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [artPiece, setArtPiece] = useState<ArtPiece | null>(null);
  const [reviews, setReviews] = useState<Review[]>([]);
  const [relatedArtPieces, setRelatedArtPieces] = useState<ArtPiece[]>([]);
  const [showAllReviews, setShowAllReviews] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      if (id) {
        const artPieceId = parseInt(id);
        const [artPieceData, reviewsData, relatedData] = await Promise.all([
          getArtPiece(artPieceId),
          getReviews(artPieceId),
          getRelatedArtPieces(artPieceId),
        ]);
        setArtPiece(artPieceData);
        setReviews(reviewsData);
        setRelatedArtPieces(relatedData);
      }
    };
    fetchData();
  }, [id]);

  if (!artPiece) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <img
          src={artPiece.image_path}
          alt={artPiece.title}
          className="w-full h-auto"
        />
        <div>
          <h1 className="text-3xl font-bold mb-4">{artPiece.title}</h1>
          <p className="text-xl mb-2">by {artPiece.author.username}</p>
          <p className="text-lg mb-4">
            Global Rating: {artPiece.global_rating.toFixed(1)}/5
          </p>
          <p className="mb-4">{artPiece.description}</p>
          <div className="mb-4">
            {artPiece.tags.map((tag) => (
              <span
                key={tag.id}
                className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
              >
                {tag.name}
              </span>
            ))}
          </div>
        </div>
      </div>

      <h2 className="text-2xl font-bold mt-8 mb-4">Recent Reviews</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {(showAllReviews ? reviews : reviews.slice(0, 5)).map((review) => (
          <ReviewCard key={review.id} review={review} />
        ))}
      </div>
      {reviews.length > 5 && (
        <div className="text-center mt-4">
          <Button onClick={() => setShowAllReviews(!showAllReviews)}>
            {showAllReviews ? "Show Less" : "Show More"}
          </Button>
        </div>
      )}

      {/* <h2 className="text-2xl font-bold mt-8 mb-4">Related Art Pieces</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
        {relatedArtPieces.slice(0, 10).map((relatedArtPiece) => (
          <ArtPieceCard key={relatedArtPiece.id} artPiece={relatedArtPiece} />
        ))}
      </div> */}
    </div>
  );
};

export default ArtPieceDetailPage;
